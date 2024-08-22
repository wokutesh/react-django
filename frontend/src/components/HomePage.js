import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchCategories } from '../redux/action/categoriesActions';
import { fetchProducts } from '../redux/action/productsActions';

import CategoryList from '../components/CategoryList';
import FlashSaleProducts from '../components/FlashSaleProducts';
import TopSellingProducts from '../components/TopSellingProducts';
import CategoryProducts from '../components/CategoryProducts';

const HomePage = () => {
  const dispatch = useDispatch();
  const categories = useSelector((state) => state.categories);
  const products = useSelector((state) => state.products);

  useEffect(() => {
    dispatch(fetchCategories());
    dispatch(fetchProducts());
  }, [dispatch]);

  return (
    <>
      <div className="row">
        <div className="col-md-3">
          <CategoryList categories={categories} />
        </div>
        <div className="col-md-9">
          <FlashSaleProducts products={products} />
        </div>
      </div>
      <div className="row">
        <TopSellingProducts products={products} />
      </div>
      {categories.map((category) => (
        <div key={category.id} className="row">
          <CategoryProducts category={category} products={products} />
        </div>
      ))}
    </>
  );
};

export default HomePage;
