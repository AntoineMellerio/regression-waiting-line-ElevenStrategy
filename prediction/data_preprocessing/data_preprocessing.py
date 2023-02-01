import sys
from DataFactory import DataFactory
from MergeDataSource import MergeDataSource

def main(argv):
    data_path = argv[0]
    output_name = argv[1]
    datafactory = DataFactory()

    df = MergeDataSource(data_path)


    cleaner  = datafactory.get_formatter('Cleaning')
    cleaner.treat_datetime(df)
    cleaner.drop_bad_rows(df)
    cleaner.drop_rudundant_cols(df)


    feature = datafactory.get_formatter('Features')
    df_new = feature.modify_features(df)


    encoder = datafactory.get_formatter('Encoding')
    df_normalize = encoder.normalize(df_new)
    df_encoded = encoder.fn_cat_onehot(df_normalize)

    df_encoded.to_csv(data_path + 'processed/' + output_name)

    
if __name__ == "__main__":
   main(sys.argv[1:])