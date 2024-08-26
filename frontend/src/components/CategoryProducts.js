import React from "react";
import { Link } from "react-router-dom";
import '../styles.css';
const CategoryProducts = ({ category, products }) => {
  const categoryProducts = products.filter(
    (product) => product.category.id === category.id
  );

  return (
    <div className="category-product">
      <h3>{category.name}</h3>
      <div
        id={`category-${category.id}`}
        className="carousel slide"
        data-bs-ride="carousel"
      >
        <div className="carousel-inner">
          {categoryProducts.map((product, index) => (
            <div
              key={product.id}
              className={`carousel-item ${index === 0 ? "active" : ""}`}
            >
              <div className="card">
                <img src={product.image} alt={product.name} className="card-img-top"/>
                <div className="card-body">
                  <h5 className="card-title">{product.name}</h5>
                  <p className="card-text">{product.description}</p>
                  <p className="card-text">Price: ${product.price}</p>
                  <p className="card-text">Stock: {product.stock}</p>
                  <Link to={`products/${product.slug}`} className="btn btn-primary">
                    View Details
                  </Link>
                </div>
              </div>
            </div>
          ))}
        </div>

        <button
          className="carousel-control-prev"
          type="button"
          data-bs-target={`#category-${category.id}`}
          data-bs-slide="prev"
        >
          <span className="carousel-control-prev-icon" aria-hidden="true"></span>
          <span className="visually-hidden">Previous</span>
        </button>
        <button
          className="carousel-control-next"
          type="button"
          data-bs-target={`#category-${category.id}`}
          data-bs-slide="next"
        >
          <span className="carousel-control-next-icon" aria-hidden="true"></span>
          <span className="visually-hidden">Next</span>
        </button>
      </div>
    </div>
  );
};

export default CategoryProducts;
