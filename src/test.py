from datetime import datetime, timedelta
from pandas import read_pickle, DataFrame
from tqdm import tqdm
from stats.stock_optimum import stock_optimum
from stats.distributions import make_from_df
from stats.negative_stock_expected_value import find_best_solution

def make_train_test_samples(data, time_column, time_from, time_to):
    train = data[(data[time_column] >= time_from) & (data[time_column] < time_to)]
    test = data[data[time_column] == time_to]
    return train, test

def test_model(model):
    metrics = list()
    data = read_pickle("week_dataset.pkl").fillna(0)
    for loc in tqdm(data['loc'].unique()):
        dataset = data[data['loc'] == loc]
        negative_z_count = 0
        negative_z_sum = 0
        unacceptable_z_count = 0
        n = len(dataset[dataset['week'] >= datetime(2019, 1, 1).date()]['week'].unique())
        for date in sorted(list(dataset[dataset['week'] >= datetime(2019, 1, 1).date()]['week'].unique())):
            train, test = make_train_test_samples(dataset, 'week', date - timedelta(days=365), date)
            A = stock_optimum(train[["sale", "spec_needs", "theft", "unknown", "defect"]], 0.62, 64)
            z = model(train, test, (0, A))

            if z < 0:
                negative_z_count += 1
                negative_z_sum += z

            if z <= 0 or z >= A:
                unacceptable_z_count += 1
        
        if negative_z_count == 0:
            metrics.append({'loc': loc, '-E{Zt|Zt < 0}': 0, 'P{0 < Zt < A}': 1 - unacceptable_z_count/n})
        
        else:
            metrics.append({'loc': loc, '-E{Zt|Zt < 0}': -negative_z_sum/negative_z_count, 'P{0 < Zt < A}': 1 - unacceptable_z_count/n})
    
    return DataFrame(metrics)
    

if __name__ == "__main__":
    
    # test simple math model

    def simple_model(train, test, *args):
        opt = stock_optimum(train[["sale", "spec_needs", "theft", "unknown", "defect"]], 0.62, 64)
        if not test.empty:
            return opt + test.iloc[0][["sale", "spec_needs", "theft", "unknown", "defect"]].sum()

        return 1

    r = test_model(simple_model)
    e = r['-E{Zt|Zt < 0}'].mean()
    p = r['P{0 < Zt < A}'].mean()
    r.to_pickle('simple_model_result.pkl')
    print(f"Simple model: -E{{Zt|Zt < 0}} = {e}; P{{0 < Zt < A}} = {p}")

    # test random model 

    def random_model(train, test, bounds):
        if not train.empty:
            d = make_from_df(train[["sale", "defect", "spec_needs", "theft", "unknown"]])
            z = test.iloc[0]['th_stock']
            y = find_best_solution(z, d, bounds)
            return z + y + test.iloc[0][["sale", "defect", "spec_needs", "theft", "unknown"]].sum()

        return 1
            
    r = test_model(random_model)
    e = r['-E{Zt|Zt < 0}'].mean()
    p = r['P{0 < Zt < A}'].mean()
    r.to_pickle('random_model_result.pkl')
    print(f"Random model: -E{{Zt|Zt < 0}} = {e}; P{{0 < Zt < A}} = {p}")

    
