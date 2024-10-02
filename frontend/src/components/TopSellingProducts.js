import React from "react";
import { Link } from "react-router-dom";
import '../styles.css';
const TopSellingProducts = ({ products }) => {
  const topSellingProducts = products
    .sort((a, b) => b.sales - a.sales)
    .slice(0, 5);

  return (
    <>
      <h3>Top Selling Products</h3>
      <div className="row">
        {topSellingProducts.map((product) => (
          <div key={product.id} className=" col-md-3 mb-4">
          <div className="card">
            <Link to={`/product/${product.slug}`}>
              <img src={product.image} 
              alt={product.name} 
              className="card-img-top"

              />
              </Link>

              <div className="card-body">
              <h4>{product.name}</h4>
              <h4>${product.description}</h4>
              <h4>${product.price}</h4>
              <Link to={`product/${product.slug}`} className="btn btn-primary">View Details</Link>
              </div>
            
            </div>
          </div>
        ))}
      </div>
    </>
  );
};

export default TopSellingProducts;
