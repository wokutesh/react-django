import React from 'react'
import {Link} from 'react-router-dom'

const CategoryList=({categories})=>{
    return (
        <div>
            <h3>Categories</h3>
            <ul>
                {categories.map((categories)=>(
                    <li key={CategoryList.id}>
                        <Link to={`/categories/${category.slug}`}>{category.name}</Link>
                        
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default CategoryList;