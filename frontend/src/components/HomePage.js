import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchCategories } from '../redux/action/categoriesActions';
import { fetchProducts } from '../redux/action/productsActions';
import CategoryList from '../components/CategoryList';
import FlashSaleProducts from '../components/FlashSaleProducts';
import TopSellingProducts from '../components/TopSellingProducts';
import CategoryProducts from '../components/CategoryProducts';
import '../styles.css';
const HomePage = () => {
  const dispatch = useDispatch();
  
  const categories = useSelector((state) => state.categories || []);
  const products = useSelector((state) => state.products || []);

  useEffect(() => {
    dispatch(fetchCategories());
    dispatch(fetchProducts());
  }, [dispatch]);
  
  console.log("Products: ", products);  // Check if products are fetched
  
  // Filter flash sale products and top-selling products
  const flashSaleProducts = products?.filter(product => product.is_flash_sale)?.slice(0, 5) || [];

  
  return (
    <div className='home-page'>
      <div className="row">
        <div className="col-md-3">
          {categories.length > 0 && <CategoryList categories={categories} />}
        </div>
        <div className="col-md-9">
          {flashSaleProducts.length > 0 && <FlashSaleProducts products={flashSaleProducts} />}
        </div>
      </div>
      <div className="row">
        {products.length > 0 && <TopSellingProducts products={products} />}
      </div>
      {products.length > 0 && categories.map((category) => (
        <div key={category.id} className="row">
          <CategoryProducts category={category} products={products} />
        </div>
      ))}
    </div>
  );
};

export default HomePage;
