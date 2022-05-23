import { ReactElement, useState } from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Link
} from "react-router-dom";
import Home from "./views/Home";
import Login from "./views/Login";
import Dashboard from "./views/Dashboard";
import { AuthContext } from "./utils/AuthContext";
import Authorization from "./components/Authorization";

const AppRoutes = (): ReactElement => {
  const [jwt, setJwt] = useState<string | null>(null);

  return (
    <AuthContext.Provider value={{ jwt, setJwt }}>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login setLoginToken={setJwt} />} />
        <Route path="/dashboard" element={
          <Authorization>
            <Dashboard />
          </Authorization>
        } />
      </Routes>
    </AuthContext.Provider>
  )
}

const App = (): ReactElement => {
  return (
    <Router>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/login">Login</Link>
          </li>
          <li>
            <Link to="/dashboard">Dashboard</Link>
          </li>
        </ul>
      </nav>
      <AppRoutes />
    </Router>
  )
}

export default App;
