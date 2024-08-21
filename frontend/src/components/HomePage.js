import React,{useEffect} from 'react'
import {useDispatch,useSelector} from 'react-redux'
import {fetchCategories} from '../redux/action/categoriesActions'
import {fetchProducts} from '../redux/action/productsActions'