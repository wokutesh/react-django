import React from "react";
import { Link } from "react-router-dom";
import '../styles.css';

const CategoryProducts = ({ category, products }) => {
  
  
  const categoryProducts = products.filter(
    
    (product) =>{console.log("Product Category ID:", product.category.id);
      return  product.category.id === category.id
    }
  );
  

  return (
    <div className="category-product">
      <h3>{category.name}</h3>
      <div className="row">
      
          {categoryProducts.map((product, index) => (
            <div key={product.id}
            className="col-md-3 mb-4"
            >
              
                <div className="card">
                  <img
                    src={product.image}
                    alt={product.name}
                    className="card-img-top" // Fix: No duplicate className
                  />
                  <div className="card-body">
                    <h5 className="card-title">{product.name}</h5>
                    <p className="card-text">{product.description}</p>
                    <p className="card-text">Price: ${product.price}</p>
                    <p className="card-text">Stock: {product.stock}</p>
                    <Link to={`/product/${product.slug}`} className="btn btn-primary">
                      View Details
                    </Link>
                  </div>
                </div>
              
            </div>
          ))}
        </div>

      </div>
      
  
  );
};

export default CategoryProducts;
