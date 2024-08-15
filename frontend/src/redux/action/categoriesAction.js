import axios from 'axios'

export const fetchCategories=()=>async(dispatch)=>{

   try{
    const response=await axios.get('/api/categories');
    dispatch(
        {
           type: 'SET_CATEGORIES',
           payload:response.data, 
        }
    )
   } 
   catch(error){
    console.error('Error fetching categories',error);
   }
}