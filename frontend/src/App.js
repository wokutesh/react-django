import 'bootstrap/dist/css/bootstrap.min.css';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import logo from './images/ecommerce-logo.jpg'


function App() {
  return (
    <Navbar expand="lg" className=""> {/* Assuming bg-primary as a valid Bootstrap class */}
      <Container>
      <Navbar.Brand href="#home">
          {/* Insert logo image here */}
          <img
            src={logo} // Path to your logo
            alt="Logo"
            width="30"
            height="30"
            className="d-inline-block align-top"
          />{' '}
          
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#link">Contact</Nav.Link>
          </Nav>
        </Navbar.Collapse>
        {/* Moving the input group inside the Container */}
        
      <Form className='d-flex' >
        <Form.Control
          type="text"
          
          className="form-control form-control-sm"
          placeholder="Search"
          aria-label="Search"
            />
            </Form>
      </Container>
    </Navbar>
  );
}

export default App;
