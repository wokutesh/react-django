import React, { useState, useEffect } from "react";
import { useNavigate } from 'react-router-dom';
import '../styles.css';
const FlashSaleProducts = ({ products }) => {
  const navigate = useNavigate();
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentIndex(prevIndex => (prevIndex + 1) % products.length);
    }, 3000);

    return () => clearInterval(interval);
  }, [products.length]);

  const handleClick = () => {
    const product = products[currentIndex];
    navigate(`/products/${product.slug}`);
  };

  return (
    <div className="flash-sale-slider" onClick={handleClick}>
        {products.length > 0 && (
            <img 
            key={products[currentIndex].id}
            src={products[currentIndex].image}
            alt={products[currentIndex].name}
            style={{ width: "150px", height: "150px", objectFit: "cover" }} 
            
            />
        )}
    </div>
  );
};

export default FlashSaleProducts;
