import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import PhoneInput from 'react-phone-input-2';
import 'react-phone-input-2/lib/style.css';

const CheckoutPage = ({ cart, setCart }) => {
    const navigate = useNavigate();
    const [fullName, setFullName] = useState('');
    const [email, setEmail] = useState('');
    const [phone, setPhone] = useState('');
    const [country, setCountry] = useState('');
    const [state, setState] = useState('');
    const [paymentMethod, setPaymentMethod] = useState('');

    const calculateTotal = () => {
        return cart.reduce((total, item) => total + parseFloat(item.price) * item.quantity, 0);
    };

    const handleSubmit = (e) => {
        e.preventDefault();  // Prevent form submission refresh
        console.log('Order details:', {
            fullName,
            email,
            phone,
            country,
            paymentMethod,
            total: calculateTotal(),
        });

        setCart([]);
        localStorage.removeItem('cart');

        if (paymentMethod === 'mpesa') {
            navigate('/mpesa-payment');
        } else if (paymentMethod === 'paypal') {
            navigate('/paypal');
        }
    };

    return (
        <div>
            <h1>Checkout</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="fullName">Full Name</label>
                    <input 
                        type="text"
                        id="fullName"
                        value={fullName}
                        onChange={(e) => setFullName(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="email">Email:</label>
                    <input
                        type="text"
                        id="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="phone">Phone:</label>
                    <PhoneInput
                        country={'eth'}
                        value={phone}
                        onChange={(value) => setPhone(value)}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="country">Country:</label>
                    <input
                        type="text"
                        id="country"
                        value={country}
                        onChange={(e) => setCountry(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="state">State</label>
                    <input
                        type="text"
                        id="state"
                        value={state}
                        onChange={(e) => setState(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Payment Method</label>
                    <div>
                        <input 
                            type="radio"
                            id="mpesa"
                            name="paymentMethod"
                            value="mpesa"
                            checked={paymentMethod === 'mpesa'}
                            onChange={(e) => setPaymentMethod(e.target.value)}
                        />
                        <label>Pay with Mpesa</label>
                    </div>
                    <div>
                        <input 
                            type="radio"
                            id="paypal"
                            name="paymentMethod"
                            value="paypal"
                            checked={paymentMethod === 'paypal'}
                            onChange={(e) => setPaymentMethod(e.target.value)}
                        />
                        <label>Pay with Paypal</label>
                    </div>
                </div>
                <div>
                    <h3>Order Summary</h3>
                    <p>Total: ${calculateTotal().toFixed(2)}</p>
                </div>
                <button type="submit">Place Order</button>
            </form>
        </div>
    );
};

export default CheckoutPage;
