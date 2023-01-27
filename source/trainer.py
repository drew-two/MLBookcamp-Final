#!/usr/bin/env python
# coding: utf-8

# # Trainer
# 
# Using the DEiT small model here (DEiT Small Distilled Patch 16, Image size 244 x 244) in the interest of time and space for deployment

import logging, os

import pandas as pd
import xgboost as xgb

from sklearn.feature_extraction import DictVectorizer

## Variables and settings
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

def cleanup_dataframe(df):
    # Removing uppercase and spaces
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    categorical = list(df.dtypes[df.dtypes == 'object'].index)

    for c in categorical:
        df[c] = df[c].str.lower().str.replace(' ', '_')

    # Cleaning up policy variable
    df["policy_id"] = df["policy_id"].str[2:] # Removes the first two letters (id)
    df["policy_id"] = df["policy_id"].astype("int")

    # Adding variables for the individual values of max_torque and max_power
    df[['max_torque_nm','max_torque_rpm']] = df['max_torque'].str.split("@", expand=True)
    df['max_torque_rpm'] = df["max_torque_rpm"].str[:-3].astype("int")
    df['max_torque_nm'] = df["max_torque_nm"].str[:-2].astype("float")

    df[['max_power_bhp','max_power_rpm']] = df['max_power'].str.split("@", expand=True)
    df['max_power_rpm'] = df["max_power_rpm"].str[:-3].astype("int")
    df['max_power_bhp'] = df["max_power_bhp"].str[:-3].astype("float")

    return df

if __name__ == "__main__":

    print("Loading datasets...")
    df_train = pd.read_csv("../../data/train.csv")
    df_train = cleanup_dataframe(df)

    dv = DictVectorizer(sparse=False)
    features = dv.get_feature_names_out()

    train_dict = df_train[categorical + numerical].to_dict(orient='records')
    X_train = dv.fit_transform(train_dict)
    y_train = df_train['is_claim']

    # Don't fit on validation dataset
    val_dict = df_val[categorical + numerical].to_dict(orient='records')
    X_val = dv.transform(val_dict)
    y_val = df_val['is_claim']

    dtrain = xgb.DMatrix(X_train, label=y_train, feature_names=features)
    dval = xgb.DMatrix(X_val, label=y_val, feature_names=features)

    # Build and train model
    print("Loading model...")
    model = build_model()
    callbacks = get_callbacks()

    print("Training model...")
    history = model.fit(
        x = train_generator,
        validation_data=val_generator,
        batch_size=BATCH_SIZE,
        epochs=EPOCHS,
        workers=WORKERS,
        callbacks=callbacks
    )

    print("Saving model...")
    model.save(filepath=MODEL_PATH)

    print("Packaging bento...")
    bentoml_model = bentoml.keras.save_model(
        "kitchenware-classification", 
        model,
        signatures={"__call__": {"batchable": True, "batch_dim": 0}}
    )

    print(bentoml_model.path)