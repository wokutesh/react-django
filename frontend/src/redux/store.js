import {configureStore,applyMiddleware,combineReducers} from 'redux';
import thunk from 'redux-thunk'
import categoriesReducers from '../reducers/categoriesReducers'

import productsReducers from '../reducers/productsReducers'


const rootReducer=combineReducer({
    categories:categoriesReducers,
    products:productsReducers
})

const store=configureStore(rootReducer,applyMiddleware(thunk))

export default store;
