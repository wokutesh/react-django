import React from 'react'
import {Link} from 'react-router-dom'

const ProductCard = ({product}) =>{
  return (
    <div className='card'>
        <img src={product.image} className="my_img" alt={product.name} />
        <div className='card-body'>
            <h5 className="card-title" 
            >{product.name}</h5>
            <p className='card-text'>{product.description}</p>
            <p>Price: ${product.price }</p>
            <Link to={`/product/${product.slug}`} className='btn btn-primary'>View Detail</Link>
        </div>
    </div>
  )
}

export default ProductCard 