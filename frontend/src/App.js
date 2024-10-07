import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, useNavigate, Link } from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Form from 'react-bootstrap/Form';
import HomePage from './components/HomePage';
import ProductDetails from './components/ProductDetails';
import SearchResultsPage from './components/SearchResultsPage';
import CategoryPage from './components/CategoryPage';
import CartPage from './components/CartPage';
import CheckoutPage from './components/CheckoutPage';

function SearchBar({ cart }) {
  const [searchQuery, setSearchQuery] = useState('');
  const navigate = useNavigate();

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
    <Form className="d-flex" role="search" onSubmit={handleSearchSubmit}>
      <Form.Control
        type="search"
        placeholder="Search"
        className="me-2"
        aria-label="Search"
        value={searchQuery}
        onChange={handleSearchChange}
      />
    </Form>
  );
}

function App() {
  const [cart, setCart] = useState(
    localStorage.getItem('cart') !== null ? JSON.parse(localStorage.getItem('cart')) : []
  );

  return (
    <div>
      <Router>
        <Navbar expand="lg" className="bg-body-tertiary">
          <Container>
            <Navbar.Brand as={Link} to="/">MyShopping</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="me-auto">
                <Nav.Link as={Link} to="/">Home</Nav.Link>
                <Nav.Link as={Link} to="/about">About</Nav.Link>
                <NavDropdown title="Category" id="basic-nav-dropdown">
                  <NavDropdown.Item as={Link} to="/categories/women-cloth">Women Cloth</NavDropdown.Item>
                  <NavDropdown.Item as={Link} to="/categories/fruits">Fruits</NavDropdown.Item>
                  <NavDropdown.Item as={Link} to="/categories/men-cloth">Men Cloth</NavDropdown.Item>
                  <NavDropdown.Item as={Link} to="/categories/food">Food</NavDropdown.Item>
                  <NavDropdown.Divider />
                  <NavDropdown.Item as={Link} to="/account">My account</NavDropdown.Item>
                </NavDropdown>
                <Nav.Link as={Link} to="/cart">Cart ({cart.length})</Nav.Link>
              </Nav>
              <SearchBar cart={cart} /> {/* Pass cart to SearchBar */}
            </Navbar.Collapse>
          </Container>
        </Navbar>

        <Container>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="product/:slug" element={<ProductDetails />} />
            <Route path="/search" element={<SearchResultsPage />} />
            <Route path="/cart" element={<CartPage cart={cart} setCart={setCart} />} />
            <Route path="/checkout" element={<CheckoutPage cart={cart} setCart={setCart} />} />
            <Route path="/categories/:slug" element={<CategoryPage />} />
          </Routes>
        </Container>
      </Router>

      <footer className="bg-success">© 2024 | Designed by Wokuma | All Rights Reserved</footer>
    </div>
  );
}

export default App;
