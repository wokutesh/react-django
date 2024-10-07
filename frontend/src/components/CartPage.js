import React from 'react';
import { Link,useNavigate } from 'react-router-dom';

const CartPage = ({ cart, setCart }) => {

  const navigate=useNavigate();
  const handleRemoveFromCart = (itemToRemove) => {
    const updatedCart = cart.filter((item) => item.id !== itemToRemove.id);
    localStorage.setItem('cart', JSON.stringify(updatedCart));
    setCart(updatedCart);
  };

  const handleUpdateQuantity = (item, newQuantity) => {
    const updatedCart = cart.map((cartItem) => {
      if (cartItem.id === item.id) {
        return {
          ...cartItem,
          quantity: newQuantity,
        };
      }
      return cartItem;
    });
    localStorage.setItem('cart', JSON.stringify(updatedCart));
    setCart(updatedCart);
  };

  const calculateTotal = () => {
    return cart.reduce((total, item) => total + parseFloat( item.price) * item.quantity, 0);
  };

  const handleCheckout =()=>{
    navigate('/checkout')
  }

  return (
    <>
      <h1>Your Cart</h1>
      {cart.length === 0 ? (
        <p>Your cart is empty</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {cart.map((item) => (
              <tr key={item.id}>
                <td>
                  <Link to={`/product/${item.slug}`}>{item.name}</Link>
                </td>
                <td>${parseFloat(item.price).toFixed(2)}</td>
                <td>
                  <input
                    type='number'
                    min='1'
                    value={item.quantity}
                    onChange={(e) => handleUpdateQuantity(item, parseInt(e.target.value))}
                  />
                </td>
                <td>${parseFloat((item.price )* item.quantity).toFixed(2)}</td>
                <td>
                  <button onClick={() => handleRemoveFromCart(item)}>Remove</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
      <div>
        <h2>Total: ${calculateTotal().toFixed(2)}</h2>
        <button onClick={handleCheckout}>Proceed to Checkout</button>
      </div>
    </>
  );
};

export default CartPage;
