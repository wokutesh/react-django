import React from 'react';
import { Link } from 'react-router-dom';
import '../styles.css'
const ProductDetails = ({ product, products }) => {
    if (!product) return null; // Check if product exists

    const currentCategory = product.category;

    const relatedProducts = products.filter(p => p.category === currentCategory && p.id !== product.id);

    return (
        <div className="product-details">
            <div className="product-image">
                <img src={product.image} alt={product.name} />
            </div>
            <div className="product-info">
                <h2>{product.name}</h2>
                <p>{product.description}</p>

                {/* <button onClick={handleAddToCart}>Add to Cart</button>
                <button onClick={handleRemoveFromCart}>Remove from Cart</button> */}
            </div>

            <div className="vendor-info">
                <h3>Vendor Information</h3>
                <p>Vendor: <Link to={`vendor/${product.vendor.id}`}>{product.vendor.name}</Link></p>
                <p>Contact: {product.vendor.contact_details}</p>
            </div>

            <div className="shipping-info">
                <h3>Shipping Information</h3>
                <p>Shipping Address: {product.shipping_address}</p>
                <p>Shipping Policy: <a href={product.shipping_policy}>Click Here</a> for shipping policy</p>
                <p>Return Policy: <a href={product.return_policy}>Click Here</a> for return policy</p>
            </div>

            <div className="reviews">
                <h3>Customer Reviews</h3>
                {product.reviews.map(review => (
                    <div key={review.id}>
                        <p>Rating: {review.rating}</p>
                        <p>Comment: {review.comment}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default ProductDetails;
