import { Route, BrowserRouter as Router, Routes } from 'react-router-dom'
import Layout from './components/shared/Layout'
import Dashboard from './pages/Dashboard'
import StudentPerClass from "./pages/StudentPerClass"

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Layout />}>
                    <Route index element={<Dashboard />} />
                    <Route to="/cp1" element={<StudentPerClass />} />
                </Route>
                
            </Routes>
        </Router>
    )
}

export default App