import React, { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import axios from "axios";

const CategoryPage = () => {
    const { slug } = useParams();
    const [category, setCategory] = useState(null);
    const [products, setProducts] = useState([]);

    useEffect(() => {
        const fetchCategoryAndProducts = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/products/?category=${slug}`);
    
                if (response.status === 200) {
                    const data = response.data;
                    
    
                    // Log each product to see how the category field is structured
                    data.forEach(product => {
                       
                    });
    
                    // Process the data (this part may need adjustment depending on the response structure)
                    if (Array.isArray(data)) {
                        const currentCategoryProducts = data.filter(
                            (products) => products.category.slug === slug// if `slug` is a number, or convert it accordingly
                        );
                        
    
                        if (currentCategoryProducts.length > 0) {
                            setCategory(currentCategoryProducts[0].category);
                            setProducts(currentCategoryProducts);
                        } else {
                            console.error("Category not found in response data.");
                        }
                    } else {
                        console.error("Invalid data format from API", data);
                    }
                } else {
                    console.error('Failed to fetch, status code:', response.status);
                }
            } catch (error) {
                console.error("Error fetching category and products:", error);
                if (error.response) {
                 
                }
            }
        };
    
        fetchCategoryAndProducts();
    }, [slug]);
    
    

    if (!category || products.length === 0) {
        return <div>Loading...</div>;
    }

    return (
        <>
            <h2>{category.name}</h2>
            <div className="row">
                {products.map((product) => (
                    <div key={product.id} className="col-md-3 mb-4">
                        <div className="card">
                            <img src={product.image} className="my_img" alt={product.name} />
                            <div className="card-body">
                                <h5 className="card-title">{product.name}</h5>
                                <p className="card-text">{product.description}</p>
                                <p className="card-text">Price: ${product.price}</p>
                                <p className="card-text">Stock: {product.stock} remaining</p>
                                <Link to={`/product/${product.slug}`} className="btn btn-primary">
                                    View Detail
                                </Link>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </>
    );
};

export default CategoryPage;
