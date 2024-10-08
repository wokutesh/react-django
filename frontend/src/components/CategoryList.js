import React from 'react';
import { Link } from 'react-router-dom';
import '../styles.css';

const CategoryList = ({ categories = [] }) => {
  return (
    <div>
      <h3>Categories</h3>
      <ul>
        {categories.length > 0 ? (
          categories.map((category) => (
            <li key={category.id}>
              <Link to={`/categories/${category.slug}`}>{category.name}</Link>
            </li>
          ))
        ) : (
          <li>No categories available</li>
        )}
      </ul>
    </div>
  );
};

export default CategoryList;
