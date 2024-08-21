import axios from 'axios'

export const fetchProducts=()=>async(dispatch)=>{

    try{
        const response= await axios.get('/api/products/')
        dispatch({
            type: 'SET_PRODUCTS',
            payload:response.data,

        })
    }
    catch(error){
        console.error('Error fetching products',error );

    }

}
