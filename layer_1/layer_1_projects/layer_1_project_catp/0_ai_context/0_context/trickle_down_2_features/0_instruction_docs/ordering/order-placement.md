---
resource_id: "c4f2e166-f247-4c73-a2f9-b5f828a4b62a"
resource_type: "document"
resource_name: "order-placement"
---
# Order Placement System
*Comprehensive food ordering system for I-Eat University Food Delivery Platform*

<!-- section_id: "4d6f6b3a-ac99-4e5e-96f6-05ea9cc3251b" -->
## 📋 Overview

The I-Eat order placement system enables students to browse restaurants, select menu items, customize orders, and place food orders with campus-specific delivery locations. The system integrates with the points system for payment and provides real-time order tracking.

<!-- section_id: "3ad63dd1-f67c-4baf-9e6c-356f0bd9574a" -->
## 🎯 **Core Requirements**

<!-- section_id: "dc1ca1fb-074d-44fe-b238-e370a3d5c19f" -->
### Order Process
- **Restaurant Browsing**: View available restaurants and their menus
- **Menu Selection**: Browse menu items with descriptions, prices, and images
- **Customization**: Modify items (size, toppings, special instructions)
- **Cart Management**: Add/remove items, update quantities
- **Checkout Process**: Review order, select payment method, place order
- **Order Confirmation**: Receive order confirmation and tracking information

<!-- section_id: "bc71c3ee-9826-461a-869b-2b4481436c90" -->
### Payment Integration
- **Points Payment**: Use earned points for full or partial payment
- **Credit/Debit Cards**: Traditional payment methods via Stripe
- **Split Payment**: Combine points and card payment
- **Payment Validation**: Real-time payment processing and validation

<!-- section_id: "20d5f1ce-0381-4ed2-97c8-959bb73c82d7" -->
## 🏗️ **Technical Architecture**

<!-- section_id: "86d663f7-d22b-4529-8be5-6be1afd5dba3" -->
### Frontend Components
- **RestaurantList**: Display available restaurants
- **MenuDisplay**: Show restaurant menu items
- **MenuItem**: Individual menu item with customization options
- **ShoppingCart**: Cart management and checkout
- **CheckoutForm**: Payment and delivery information
- **OrderConfirmation**: Order summary and tracking

<!-- section_id: "a30aced9-3827-4774-85ca-f2f098be838c" -->
### Backend Services
- **Menu API**: Restaurant and menu data management
- **Order API**: Order creation and management
- **Payment API**: Payment processing integration
- **Points API**: Points balance and redemption
- **Location API**: Campus delivery locations

<!-- section_id: "d45545ae-77ec-4226-8254-0a796058c9be" -->
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

<!-- section_id: "3c175c79-8184-4ceb-8bb8-40fad5db34fc" -->
## 🎨 **User Interface**

<!-- section_id: "54b94fb4-1128-43c6-943b-bb9f4eb8b50e" -->
### Restaurant Browsing
- **Grid Layout**: Card-based restaurant display
- **Filter Options**: Cuisine type, rating, delivery time
- **Search Functionality**: Search by restaurant name or cuisine
- **Sort Options**: By rating, delivery time, or distance
- **Restaurant Cards**: Name, image, rating, delivery time, minimum order

<!-- section_id: "c8bdfae4-d7a4-4c33-b9e5-48a4c7c88df2" -->
### Menu Display
- **Category Tabs**: Organize menu items by category
- **Item Cards**: Image, name, description, price, availability
- **Customization Modal**: Size options, toppings, special instructions
- **Add to Cart**: Quantity selector and add button
- **Nutritional Info**: Optional nutritional information display

<!-- section_id: "7df38a91-7b62-4a86-afab-0b30f6cedab4" -->
### Shopping Cart
- **Item List**: Selected items with quantities and prices
- **Modify Options**: Edit quantities, remove items, update customizations
- **Price Breakdown**: Subtotal, delivery fee, tax, total
- **Points Display**: Available points and redemption options
- **Checkout Button**: Proceed to checkout

<!-- section_id: "256270d8-ee5b-4d19-8419-b8fa4c5fc66d" -->
### Checkout Process
- **Order Summary**: Review all items and prices
- **Delivery Information**: Select campus location and special instructions
- **Payment Method**: Choose between points, card, or split payment
- **Points Redemption**: Select amount of points to use
- **Place Order**: Final order submission

<!-- section_id: "d7fe6ac8-736b-482c-a282-a83c3c949489" -->
## 🔄 **User Flows**

<!-- section_id: "09e0ea5d-9638-4044-982b-f4205bd9081e" -->
### Basic Order Flow
1. **Browse Restaurants**: User views available restaurants
2. **Select Restaurant**: User chooses a restaurant
3. **Browse Menu**: User views menu items and categories
4. **Add Items**: User adds items to cart with customizations
5. **Review Cart**: User reviews selected items and prices
6. **Checkout**: User proceeds to checkout
7. **Payment**: User selects payment method and pays
8. **Confirmation**: User receives order confirmation

<!-- section_id: "a1c65b5b-9eae-4bd9-af4d-5f6214f7a15b" -->
### Points Redemption Flow
1. **View Points**: User sees available points balance
2. **Select Redemption**: User chooses to use points
3. **Enter Amount**: User specifies points to redeem
4. **Calculate Balance**: System calculates remaining balance
5. **Complete Payment**: User pays remaining amount if any
6. **Update Points**: System updates points balance

<!-- section_id: "a6641adf-716b-407d-9958-3e85d53ab017" -->
### Order Customization Flow
1. **Select Item**: User clicks on menu item
2. **Open Customization**: Customization modal opens
3. **Choose Options**: User selects size, toppings, etc.
4. **Add Instructions**: User adds special instructions
5. **Update Price**: System calculates updated price
6. **Add to Cart**: User adds customized item to cart

<!-- section_id: "2bec1bad-0a58-4eba-bbfc-ce4f9ed1cafb" -->
## 🧪 **Testing Requirements**

<!-- section_id: "2793bcb0-3b8f-4d67-ad5a-7cdf63e518f7" -->
### Unit Tests
- **Cart Management**: Add, remove, update cart items
- **Price Calculations**: Subtotal, tax, delivery fee calculations
- **Points Redemption**: Points balance and redemption logic
- **Order Validation**: Order data validation and error handling

<!-- section_id: "b6a8ab87-5813-4ba4-8c26-794361601789" -->
### Integration Tests
- **Menu API**: Restaurant and menu data retrieval
- **Order API**: Order creation and management
- **Payment API**: Payment processing integration
- **Points API**: Points balance and redemption

<!-- section_id: "5576f5a1-5f92-4d77-bd34-5bde64ecbcbf" -->
### E2E Tests
- **Complete Order Flow**: Full order placement process
- **Payment Processing**: Successful and failed payment scenarios
- **Points Redemption**: Points-based payment flow
- **Error Handling**: Network errors and validation failures

<!-- section_id: "ff477387-723f-4b0e-a167-66bb7b08b67c" -->
## 📊 **Performance Requirements**

<!-- section_id: "65a72265-21ac-49ee-83c6-2ee50ad85d1f" -->
### Response Times
- **Menu Loading**: < 2 seconds for restaurant menus
- **Cart Updates**: < 500ms for cart modifications
- **Order Placement**: < 3 seconds for order submission
- **Payment Processing**: < 5 seconds for payment completion

<!-- section_id: "edafea82-1771-418a-a6f8-9cc96d44788f" -->
### Scalability
- **Concurrent Orders**: Support 1,000+ simultaneous orders
- **Menu Updates**: Real-time menu availability updates
- **Cart Persistence**: Maintain cart across browser sessions
- **Order Processing**: Handle peak order volumes

<!-- section_id: "35b3f0c0-161d-4eaa-9a1c-d6aadece92f5" -->
## 🔧 **Implementation Guide**

<!-- section_id: "cf00b9f9-2b5b-48e4-9012-0ecca5d8beb7" -->
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

<!-- section_id: "0d3724f5-b755-41d5-bd4d-df2308f49a88" -->
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

<!-- section_id: "aecada88-5a8e-4866-b323-61290081c493" -->
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

<!-- section_id: "594bcbf2-d6bd-4f48-95ab-1ae7c2e1b82c" -->
## 🚀 **Deployment Considerations**

<!-- section_id: "fd8ab79d-ea49-4197-8d5a-60257947315d" -->
### Environment Variables
```bash
# Stripe configuration
VITE_STRIPE_PUBLISHABLE_KEY=your-stripe-publishable-key
STRIPE_SECRET_KEY=your-stripe-secret-key

# Supabase configuration
VITE_SUPABASE_URL=your-supabase-url
VITE_SUPABASE_ANON_KEY=your-supabase-anon-key
```

<!-- section_id: "53ac5578-c851-495a-95b5-f37234e64ce1" -->
### Security Measures
- **Input Validation**: Validate all order data
- **Payment Security**: Use Stripe's secure payment processing
- **Rate Limiting**: Implement order placement rate limiting
- **Data Encryption**: Encrypt sensitive order information

<!-- section_id: "6621ea66-a945-41c2-a2f3-e1248959cef2" -->
## 📈 **Success Metrics**

<!-- section_id: "f98ee838-d1c5-4823-82d8-60c319d039f3" -->
### User Engagement
- **Order Completion Rate**: 85%+ successful order completion
- **Cart Abandonment**: < 30% cart abandonment rate
- **Repeat Orders**: 60%+ users place repeat orders
- **Points Usage**: 70%+ of users redeem points

<!-- section_id: "cc6a8c71-d18e-417c-b248-5b34be6acabb" -->
### Business Metrics
- **Order Volume**: 1,000+ orders per month
- **Average Order Value**: $15+ per order
- **Revenue Growth**: 20% month-over-month growth
- **Customer Satisfaction**: 4.5+ star average rating

<!-- section_id: "409df78d-c66d-4b62-810a-2e663f72f4a7" -->
## 🔗 **Related Documentation**

- **Restaurant Management**: `restaurant-management.md`
- **Menu Management**: `menu-management.md`
- **Order Management**: `order-management.md`
- **Points System**: `../points/points-management.md`
- **Payment Integration**: `../technical/payment-integration.md`

---

**Last Updated**: January 24, 2025  
**Maintained By**: I-Eat Development Team
