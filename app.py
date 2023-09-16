import streamlit as st
import streamlit.components.v1 as components
import pickle
import pickle as cPickle
import bz2


def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = pickle.load(data)
    return data
    
    
path = './models/random_forest.pbz2'
model = decompress_pickle(path)

