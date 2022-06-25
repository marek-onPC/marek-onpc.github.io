import { ReactElement, useState } from "react";
import { Buffer } from "buffer";
import {
  BrowserRouter as Router,
  Route,
  Routes,
} from "react-router-dom";
import Home from "./views/Home";
import Login from "./views/Login";
import Dashboard from "./views/Dashboard";
import { AuthContext } from "./utils/AuthContext";
import Authorization from "./components/Authorization";
import { Box, ThemeProvider, Typography } from "@mui/material";
import { ThemeContext } from "./utils/ThemeContext";

let initialAuthContext = "";
const LOGIN_TOKEN = window.localStorage.getItem(
  process.env.REACT_APP_LOCAL_STORAGE_TOKEN as string
);

if (LOGIN_TOKEN) {
  const LOGIN_TOKEN_PAYLOAD = LOGIN_TOKEN.split('.')[1];
  const DECODED_PAYLOAD = Buffer.from(LOGIN_TOKEN_PAYLOAD, 'base64');
  const TOKEN_EXPIRATION = JSON.parse(DECODED_PAYLOAD.toString())["exp"] * 1000;
  const CURRENT_TIME = new Date();

  if (TOKEN_EXPIRATION > CURRENT_TIME.getTime()) {
    initialAuthContext = LOGIN_TOKEN;
  }
};

const AppRoutes = (): ReactElement => {
  const [jwt, setJwt] = useState<string>(initialAuthContext);

  return (
    <AuthContext.Provider value={jwt}>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="login" element={<Login setLoginToken={setJwt} />} />
        <Route path="dashboard" element={
          <Authorization>
            <Dashboard>
              <Typography variant="h2" color="white">welcome back</Typography>
              <Typography variant="h3" color="white">in</Typography>
              <Typography variant="h4" color="white">dashboard</Typography>
            </Dashboard>
          </Authorization>
        } />
        <Route path="dashboard/notes" element={
          <Authorization>
            <Dashboard>
              <Typography variant="h4" color="white">notes</Typography>
            </Dashboard>
          </Authorization>
        } />
        <Route path="dashboard/categories" element={
          <Authorization>
            <Dashboard>
              <Typography variant="h4" color="white">categories</Typography>
            </Dashboard>
          </Authorization>
        } />
      </Routes>
    </AuthContext.Provider>
  )
}

const App = (): ReactElement => {
  return (
    <ThemeProvider theme={ThemeContext}>
      <Box
        sx={{
          width: "100%",
          minHeight: "100vh",
          display: "flex",
          flexDirection: "column",
          bgcolor: "secondary.main"
        }}
      >
        <Router>
          <AppRoutes />
        </Router>
      </Box>
    </ThemeProvider>
  );
};

export default App;
