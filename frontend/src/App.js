import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router } from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Form from 'react-bootstrap/Form';
import logo from './images/ecommerce-logo.jpg'; // Ensure path is correct
import HomePage from './components/HomePage';

function App() {
  return (
    <Router>
      <Navbar expand="lg" className="bg-primary"> {/* Use a Bootstrap class for styling */}
        <Container>
          <Navbar.Brand href="#home">
            <img
              src={logo}
              alt="Logo"
              width="30"
              height="30"
              className="d-inline-block align-top"
            />
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="#home">Home</Nav.Link>
              <Nav.Link href="#link">Contact</Nav.Link>
            </Nav>
          </Navbar.Collapse>
          <Form className='d-flex'>
            <Form.Control
              type="text"
              className="form-control form-control-sm"
              placeholder="Search"
              aria-label="Search"
            />
          </Form>
         
        </Container>
      </Navbar>
      <HomePage />
    </Router>
  );
}

export default App;
