import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Form from 'react-bootstrap/Form';
import HomePage from './components/HomePage';
import ProductDetails from './components/ProductDetails';
import SearchResultsPage from './components/SearchResultsPage';

function SearchBar() {
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
  return (
    <Router>
      <Navbar expand="lg" className="bg-body-tertiary">
        <Container>
          <Navbar.Brand href="/">MyShopping</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="/">Home</Nav.Link>
              <Nav.Link href="/">About</Nav.Link>
              <NavDropdown title="Category" id="basic-nav-dropdown">
                <NavDropdown.Item href="/">Foodstuff</NavDropdown.Item>
                <NavDropdown.Item href="/">Fruits</NavDropdown.Item>
                <NavDropdown.Item href="/">Fashion</NavDropdown.Item>
                <NavDropdown.Item href="/">Electronics</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item href="/">My account</NavDropdown.Item>
              </NavDropdown>
            </Nav>
            <SearchBar /> {/* Move the search logic into this SearchBar component */}
          </Navbar.Collapse>
        </Container>
      </Navbar>

      <Container>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="products/:slug" element={<ProductDetails />} />
          <Route path="/search" element={<SearchResultsPage />} />
        </Routes>
      </Container>
    </Router>
  );
}

export default App;
