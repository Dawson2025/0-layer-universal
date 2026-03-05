---
resource_id: "eef572cc-d7cd-44ba-8c41-dd6e2f97d807"
resource_type: "document"
resource_name: "order-placement"
---
# Order Placement System
*Comprehensive food ordering system for I-Eat University Food Delivery Platform*

<!-- section_id: "64025584-a1c8-4ce4-8d17-873a2f610832" -->
## 📋 Overview

The I-Eat order placement system enables students to browse restaurants, select menu items, customize orders, and place food orders with campus-specific delivery locations. The system integrates with the points system for payment and provides real-time order tracking.

<!-- section_id: "f6340052-e860-485e-b627-50a65bb2366b" -->
## 🎯 **Core Requirements**

<!-- section_id: "db56e074-7301-4495-9a58-070cd3306a12" -->
### Order Process
- **Restaurant Browsing**: View available restaurants and their menus
- **Menu Selection**: Browse menu items with descriptions, prices, and images
- **Customization**: Modify items (size, toppings, special instructions)
- **Cart Management**: Add/remove items, update quantities
- **Checkout Process**: Review order, select payment method, place order
- **Order Confirmation**: Receive order confirmation and tracking information

<!-- section_id: "633e59a3-9f4a-4b36-a9ba-2493e1a16f38" -->
### Payment Integration
- **Points Payment**: Use earned points for full or partial payment
- **Credit/Debit Cards**: Traditional payment methods via Stripe
- **Split Payment**: Combine points and card payment
- **Payment Validation**: Real-time payment processing and validation

<!-- section_id: "f107a852-4acf-48bd-8e86-7bc191b0d1f7" -->
## 🏗️ **Technical Architecture**

<!-- section_id: "8f63cda0-ca81-469f-a4cf-5d79f7403b24" -->
### Frontend Components
- **RestaurantList**: Display available restaurants
- **MenuDisplay**: Show restaurant menu items
- **MenuItem**: Individual menu item with customization options
- **ShoppingCart**: Cart management and checkout
- **CheckoutForm**: Payment and delivery information
- **OrderConfirmation**: Order summary and tracking

<!-- section_id: "e6abbba1-cb24-4c2d-b025-3ddb1929f982" -->
### Backend Services
- **Menu API**: Restaurant and menu data management
- **Order API**: Order creation and management
- **Payment API**: Payment processing integration
- **Points API**: Points balance and redemption
- **Location API**: Campus delivery locations

<!-- section_id: "09ef4dbe-a834-40fa-8aaa-d64f2e6d975d" -->
### Database Schema
```sql
-- Restaurants table
CREATE TABLE public.restaurants (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT,
  image_url TEXT,
  cuisine_type TEXT,
  rating DECIMAL(3,2),
  delivery_fee DECIMAL(10,2) DEFAULT 0,
  minimum_order DECIMAL(10,2) DEFAULT 0,
  estimated_delivery_time INTEGER, -- minutes
  is_active BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Menu items table
CREATE TABLE public.menu_items (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  restaurant_id UUID REFERENCES public.restaurants(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  description TEXT,
  price DECIMAL(10,2) NOT NULL,
  image_url TEXT,
  category TEXT,
  is_available BOOLEAN DEFAULT TRUE,
  preparation_time INTEGER, -- minutes
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Orders table
CREATE TABLE public.orders (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id UUID REFERENCES public.users(id) ON DELETE CASCADE,
  restaurant_id UUID REFERENCES public.restaurants(id),
  order_number TEXT UNIQUE NOT NULL,
  status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'confirmed', 'preparing', 'ready', 'out_for_delivery', 'delivered', 'cancelled')),
  subtotal DECIMAL(10,2) NOT NULL,
  delivery_fee DECIMAL(10,2) DEFAULT 0,
  tax DECIMAL(10,2) DEFAULT 0,
  total DECIMAL(10,2) NOT NULL,
  points_used DECIMAL(10,2) DEFAULT 0,
  payment_method TEXT NOT NULL,
  delivery_location TEXT NOT NULL,
  special_instructions TEXT,
  estimated_delivery_time TIMESTAMP WITH TIME ZONE,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Order items table
CREATE TABLE public.order_items (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  order_id UUID REFERENCES public.orders(id) ON DELETE CASCADE,
  menu_item_id UUID REFERENCES public.menu_items(id),
  quantity INTEGER NOT NULL DEFAULT 1,
  unit_price DECIMAL(10,2) NOT NULL,
  total_price DECIMAL(10,2) NOT NULL,
  special_instructions TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

<!-- section_id: "9564172d-aef3-43f3-a648-e18597734d54" -->
## 🎨 **User Interface**

<!-- section_id: "ba77533b-ad49-4b0f-a532-c4717d2d647b" -->
### Restaurant Browsing
- **Grid Layout**: Card-based restaurant display
- **Filter Options**: Cuisine type, rating, delivery time
- **Search Functionality**: Search by restaurant name or cuisine
- **Sort Options**: By rating, delivery time, or distance
- **Restaurant Cards**: Name, image, rating, delivery time, minimum order

<!-- section_id: "92ac890f-b0f5-4f12-91fd-837ac722975a" -->
### Menu Display
- **Category Tabs**: Organize menu items by category
- **Item Cards**: Image, name, description, price, availability
- **Customization Modal**: Size options, toppings, special instructions
- **Add to Cart**: Quantity selector and add button
- **Nutritional Info**: Optional nutritional information display

<!-- section_id: "845a28ae-6781-49c3-b791-f0c87ad46e6a" -->
### Shopping Cart
- **Item List**: Selected items with quantities and prices
- **Modify Options**: Edit quantities, remove items, update customizations
- **Price Breakdown**: Subtotal, delivery fee, tax, total
- **Points Display**: Available points and redemption options
- **Checkout Button**: Proceed to checkout

<!-- section_id: "c57da9e7-294c-4fe6-9150-559cb6046f3e" -->
### Checkout Process
- **Order Summary**: Review all items and prices
- **Delivery Information**: Select campus location and special instructions
- **Payment Method**: Choose between points, card, or split payment
- **Points Redemption**: Select amount of points to use
- **Place Order**: Final order submission

<!-- section_id: "f98fea44-c7fd-4b93-988a-b79487a600ad" -->
## 🔄 **User Flows**

<!-- section_id: "d9e252ad-234b-4560-9a34-6f39ddfa0159" -->
### Basic Order Flow
1. **Browse Restaurants**: User views available restaurants
2. **Select Restaurant**: User chooses a restaurant
3. **Browse Menu**: User views menu items and categories
4. **Add Items**: User adds items to cart with customizations
5. **Review Cart**: User reviews selected items and prices
6. **Checkout**: User proceeds to checkout
7. **Payment**: User selects payment method and pays
8. **Confirmation**: User receives order confirmation

<!-- section_id: "5ca7258f-16c4-4263-b288-0e619f581619" -->
### Points Redemption Flow
1. **View Points**: User sees available points balance
2. **Select Redemption**: User chooses to use points
3. **Enter Amount**: User specifies points to redeem
4. **Calculate Balance**: System calculates remaining balance
5. **Complete Payment**: User pays remaining amount if any
6. **Update Points**: System updates points balance

<!-- section_id: "509e6acb-f9be-4f75-97fe-d7eb4def6bf2" -->
### Order Customization Flow
1. **Select Item**: User clicks on menu item
2. **Open Customization**: Customization modal opens
3. **Choose Options**: User selects size, toppings, etc.
4. **Add Instructions**: User adds special instructions
5. **Update Price**: System calculates updated price
6. **Add to Cart**: User adds customized item to cart

<!-- section_id: "661c6ad0-ead2-4e75-856f-648401722852" -->
## 🧪 **Testing Requirements**

<!-- section_id: "f1295b0e-e3ed-48f5-aacb-b76bdc4a727b" -->
### Unit Tests
- **Cart Management**: Add, remove, update cart items
- **Price Calculations**: Subtotal, tax, delivery fee calculations
- **Points Redemption**: Points balance and redemption logic
- **Order Validation**: Order data validation and error handling

<!-- section_id: "3d1b6b32-339f-4005-93dd-f05941110da3" -->
### Integration Tests
- **Menu API**: Restaurant and menu data retrieval
- **Order API**: Order creation and management
- **Payment API**: Payment processing integration
- **Points API**: Points balance and redemption

<!-- section_id: "59b4d643-1d2e-4f47-b2b8-b095fbbbe216" -->
### E2E Tests
- **Complete Order Flow**: Full order placement process
- **Payment Processing**: Successful and failed payment scenarios
- **Points Redemption**: Points-based payment flow
- **Error Handling**: Network errors and validation failures

<!-- section_id: "eb3db6d0-a107-4fc6-9310-4defbf074601" -->
## 📊 **Performance Requirements**

<!-- section_id: "baa9910e-f36e-457f-a8ff-33f3ab15c6ee" -->
### Response Times
- **Menu Loading**: < 2 seconds for restaurant menus
- **Cart Updates**: < 500ms for cart modifications
- **Order Placement**: < 3 seconds for order submission
- **Payment Processing**: < 5 seconds for payment completion

<!-- section_id: "54de840e-9036-4551-835c-3ee91fbd06cc" -->
### Scalability
- **Concurrent Orders**: Support 1,000+ simultaneous orders
- **Menu Updates**: Real-time menu availability updates
- **Cart Persistence**: Maintain cart across browser sessions
- **Order Processing**: Handle peak order volumes

<!-- section_id: "fc0e619f-4c9f-4f32-8d58-a91ebf4f3fb3" -->
## 🔧 **Implementation Guide**

<!-- section_id: "1935e81c-9919-4c96-b87d-eb475deb9428" -->
### Frontend Components
```javascript
// src/components/ordering/RestaurantList.jsx
import React, { useState, useEffect } from 'react'
import { supabase } from '../../lib/supabase'

const RestaurantList = () => {
  const [restaurants, setRestaurants] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchRestaurants()
  }, [])

  const fetchRestaurants = async () => {
    try {
      const { data, error } = await supabase
        .from('restaurants')
        .select('*')
        .eq('is_active', true)
        .order('rating', { ascending: false })

      if (error) throw error
      setRestaurants(data)
    } catch (error) {
      console.error('Error fetching restaurants:', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="restaurant-list">
      {loading ? (
        <div>Loading restaurants...</div>
      ) : (
        restaurants.map(restaurant => (
          <RestaurantCard key={restaurant.id} restaurant={restaurant} />
        ))
      )}
    </div>
  )
}

export default RestaurantList
```

<!-- section_id: "38bbf7f9-5923-4c38-b5c5-3af67665c428" -->
### Cart Management
```javascript
// src/hooks/useCart.js
import { useState, useEffect } from 'react'

export const useCart = () => {
  const [cart, setCart] = useState([])
  const [total, setTotal] = useState(0)

  const addToCart = (item, customizations = {}) => {
    const cartItem = {
      id: `${item.id}-${Date.now()}`,
      menuItem: item,
      quantity: 1,
      customizations,
      price: item.price
    }

    setCart(prev => [...prev, cartItem])
  }

  const updateQuantity = (itemId, quantity) => {
    if (quantity <= 0) {
      removeFromCart(itemId)
      return
    }

    setCart(prev =>
      prev.map(item =>
        item.id === itemId ? { ...item, quantity } : item
      )
    )
  }

  const removeFromCart = (itemId) => {
    setCart(prev => prev.filter(item => item.id !== itemId))
  }

  const clearCart = () => {
    setCart([])
  }

  useEffect(() => {
    const newTotal = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0)
    setTotal(newTotal)
  }, [cart])

  return {
    cart,
    total,
    addToCart,
    updateQuantity,
    removeFromCart,
    clearCart
  }
}
```

<!-- section_id: "bea3d29e-0145-4ff2-be7d-8eaaf9b7b523" -->
### Order Placement
```javascript
// src/services/orderService.js
import { supabase } from '../lib/supabase'

export const createOrder = async (orderData) => {
  try {
    const { data, error } = await supabase
      .from('orders')
      .insert([orderData])
      .select()
      .single()

    if (error) throw error
    return { data, error: null }
  } catch (error) {
    console.error('Error creating order:', error)
    return { data: null, error }
  }
}

export const getOrder = async (orderId) => {
  try {
    const { data, error } = await supabase
      .from('orders')
      .select(`
        *,
        restaurant:restaurants(*),
        order_items:order_items(
          *,
          menu_item:menu_items(*)
        )
      `)
      .eq('id', orderId)
      .single()

    if (error) throw error
    return { data, error: null }
  } catch (error) {
    console.error('Error fetching order:', error)
    return { data: null, error }
  }
}
```

<!-- section_id: "765ba3da-0d6b-42c4-9ea8-e72a4555825c" -->
## 🚀 **Deployment Considerations**

<!-- section_id: "ad448df2-ae84-4e12-8c1f-0a26b1d3c1e3" -->
### Environment Variables
```bash
# Stripe configuration
VITE_STRIPE_PUBLISHABLE_KEY=your-stripe-publishable-key
STRIPE_SECRET_KEY=your-stripe-secret-key

# Supabase configuration
VITE_SUPABASE_URL=your-supabase-url
VITE_SUPABASE_ANON_KEY=your-supabase-anon-key
```

<!-- section_id: "115a0698-d11e-4428-baff-1ab77c3bb5b2" -->
### Security Measures
- **Input Validation**: Validate all order data
- **Payment Security**: Use Stripe's secure payment processing
- **Rate Limiting**: Implement order placement rate limiting
- **Data Encryption**: Encrypt sensitive order information

<!-- section_id: "e692939e-ed78-4003-9097-e45100e96d8b" -->
## 📈 **Success Metrics**

<!-- section_id: "8b89f243-136e-459e-a859-14a8da905a1c" -->
### User Engagement
- **Order Completion Rate**: 85%+ successful order completion
- **Cart Abandonment**: < 30% cart abandonment rate
- **Repeat Orders**: 60%+ users place repeat orders
- **Points Usage**: 70%+ of users redeem points

<!-- section_id: "23f0df85-eeaf-42b3-9854-ccfd9ccac99b" -->
### Business Metrics
- **Order Volume**: 1,000+ orders per month
- **Average Order Value**: $15+ per order
- **Revenue Growth**: 20% month-over-month growth
- **Customer Satisfaction**: 4.5+ star average rating

<!-- section_id: "7d06d018-4c2b-4881-a8c6-00f9d9bb2e03" -->
## 🔗 **Related Documentation**

- **Restaurant Management**: `restaurant-management.md`
- **Menu Management**: `menu-management.md`
- **Order Management**: `order-management.md`
- **Points System**: `../points/points-management.md`
- **Payment Integration**: `../technical/payment-integration.md`

---

**Last Updated**: January 24, 2025  
**Maintained By**: I-Eat Development Team
