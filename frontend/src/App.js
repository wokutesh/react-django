import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Routes, useNavigate, Link } from 'react-router-dom';
import HomePage from './components/HomePage';
import ProductDetails from './components/ProductDetails';
import SearchResultsPage from './components/SearchResultsPage';
import CategoryPage from './components/CategoryPage';
import CartPage from './components/CartPage';
import CheckoutPage from './components/CheckoutPage';
import { useDispatch, useSelector } from 'react-redux';
import { loadUser } from './action/authActions';
import Signup from './components/Signup';
import Login from './components/Login';
import Logout from './components/Logout';
import Profile from './components/Profile';
import VerifyEmail from './components/VerifyEmail';
import ProtectedRoute from './components/ProtectedRoute';
import PasswordResetRequest from './components/PasswordResetRequest';
import PasswordResetConfirm from './components/PasswordResetConfirm';


function SearchBar({ cart }) {
  const [searchQuery, setSearchQuery] = useState('');
  const navigate = useNavigate();

  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(loadUser());
  }, [dispatch]);

  const handleSearchChange = (event) => {
    setSearchQuery(event.target.value);
  };

  const handleSearchSubmit = (event) => {
    event.preventDefault();
    if (searchQuery.trim() !== '') {
      navigate(`/search?q=${searchQuery}`);
    }
  };

  return (
    <form className="flex" role="search" onSubmit={handleSearchSubmit}>
      <input
        type="search"
        placeholder="Search"
        className="p-2 rounded-xl border border-gray-300  h-10 w-96"
        aria-label="Search"
        value={searchQuery}
        onChange={handleSearchChange}
      />
    </form>
  );
}

function App() {
  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);
  const [cart, setCart] = useState(
    localStorage.getItem('cart') !== null ? JSON.parse(localStorage.getItem('cart')) : []

    
  );
  const [isCategoryOpen, setIsCategoryOpen] = useState(false);

  const handleMouseEnter = () => {
    setIsCategoryOpen(true);
  };

  const handleMouseLeave = () => {
    setIsCategoryOpen(false);
  };

  return (
    <div>
      <Router>
      <nav className="bg-gray-800 p-4">
  <div className="container mx-auto flex justify-between items-center">
    <Link to="/" className="text-white ml-24 text-lg font-bold">
      MyShopping
    </Link>

    <SearchBar cart={cart} />

    <div className="relative group" onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave}>
    <button
           
            className="text-white focus:outline-none"
          >
            Category
          </button>
          {isCategoryOpen && (
      <div className="absolute hidden group-hover:grid grid-cols-3 w-max -ml-64 mt-4 hover:grid-cols-3
       bg-white text-gray-700 rounded-lg shadow-md p-4 gap-4 top-full left-0 z-50">
        <Link to="/categories/engine" className="block p-2">Engine</Link>
        <Link to="/categories/transmission-system" className="block p-2">Transmission System</Link>
        <Link to="/categories/brake-system" className="block p-2">Brake System</Link>
        <Link to="/categories/steering-system" className="block p-2">Steering System</Link>
        <Link to="/categories/walking-system" className="block p-2">Walking System</Link>
        <Link to="/categories/automobile-exterior" className="block p-2">Automobile Exterior</Link>
        <Link to="/categories/automobile-lamps" className="block p-2">Automobile Lamps</Link>
        <Link to="/categories/auto-modification" className="block p-2">Auto Modification</Link>
        <Link to="/categories/security" className="block p-2">Security</Link>
        <Link to="/categories/car-interior" className="block p-2">Car Interior</Link>
        <Link to="/categories/electrical-instrument" className="block p-2">Electrical Instrument</Link>
        <Link to="/categories/comprehensive" className="block p-2">Comprehensive</Link>
        <Link to="/categories/audio-video-electrical" className="block p-2">Audio and Video Electrical</Link>
        <Link to="/categories/car-body" className="block p-2">Car Body</Link>
        <Link to="/categories/automotive-electrical" className="block p-2">Automotive Electrical</Link>
        <Link to="/categories/chemical-physical-accessories" className="block p-2">Chemical Physical Accessories</Link>
        <Link to="/categories/automobile-maintenance" className="block p-2">Automobile Maintenance</Link>
        <Link to="/categories/auto-parts" className="block p-2">Auto Parts</Link>
      </div>
          )}
    </div>

    <div className="space-x-4">
      <Link to="/cart" className="text-white">Cart ({cart.length})</Link>
      {isAuthenticated ? (
        <>
          <Link to="/profile" className="text-white">Profile</Link>
          <Link to="/logout" className="text-white">Logout</Link>
        </>
      ) : (
        <>
          <Link to="/login" className="text-white">Login</Link>
          <Link to="/signup" className="text-white">Register</Link>
        </>
      )}
    </div>
  </div>
</nav>


        <main className="container mx-auto py-8">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/products/:id" element={<ProductDetails />} />
            <Route path="/search" element={<SearchResultsPage />} />
            <Route path="/cart" element={<CartPage cart={cart} setCart={setCart} />} />
            <Route path="/checkout" element={<ProtectedRoute isAuthenticated={isAuthenticated}><CheckoutPage cart={cart} setCart={setCart} /></ProtectedRoute>} />
            <Route path="/categories/:slug" element={<CategoryPage />} />
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<Signup />} />
            <Route path="/logout" element={<ProtectedRoute isAuthenticated={isAuthenticated}><Logout /></ProtectedRoute>} />
            <Route path="/profile" element={<ProtectedRoute isAuthenticated={isAuthenticated}><Profile /></ProtectedRoute>} />
            <Route path="/verify-email/:uid/:token" element={<VerifyEmail />} />
            <Route path="/password-reset" element={<PasswordResetRequest />} />
            <Route path="/reset-password/:uid/:token" element={<PasswordResetConfirm />} />
          </Routes>
        </main>

        <footer className="bg-green-600 text-white text-center p-4">
          © 2024 | Designed by Wokuma | All Rights Reserved
        </footer>
      </Router>
    </div>
  );
}

export default App;
