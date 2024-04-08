import { Route, BrowserRouter as Router, Routes } from 'react-router-dom'
import Layout from './components/shared/Layout'
import Dashboard from './pages/Dashboard'
import Products from "./pages/Products"

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Layout />}>
                    <Route index element={<Dashboard />} />
                    <Route path="products" element={<Products />} />
                </Route>
                 
            </Routes>
        </Router>
    )
}

export default App