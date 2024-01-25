const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3001;

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/mupkins', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Create a Product schema
const productSchema = new mongoose.Schema({
  name: String,
  description: String,
  price: Number,
});

const Product = mongoose.model('Product', productSchema);

// Middleware
app.use(bodyParser.json());

// API to get all products
app.get('/api/products', async (req, res) => {
  try {
    const products = await Product.find();
    res.json(products);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// API to add a product to the cart
app.post('/api/addToCart', async (req, res) => {
  try {
    const { productName, productDescription, price } = req.body;
    const product = new Product({ name: productName, description: productDescription, price });
    await product.save();
    res.json({ success: true, message: 'Product added to the cart.' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
