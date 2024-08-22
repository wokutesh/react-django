import React,{useEffect} from 'react'
import {useDispatch,useSelector} from 'react-redux'
import {fetchCategories} from '../redux/action/categoriesActions'
import {fetchProducts} from '../redux/action/productsActions'

import CategoryLsit from '../components/CategoryList'
import FlashSaleProducts from '../components/FlashSaleProducts'
import TopSellingProducts from '../components/TopSellingProducts'
import CategoryProducts from '../components/CategoryProducts'

const HomePage=()=>{
   const dispatch= useDispatch();
   const categories = useSelector((state)=> state.categories)
   const products = useSelector((state)=> state.products)
   
   useEffect(()=>{
    dispatch(fetchCategories())
    dispatch(fetchProducts())
   },[dispatch])
}

return (

    <>
    
    </>
)
