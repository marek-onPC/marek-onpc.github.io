import { ReactElement, useState } from "react";
import { Buffer } from "buffer";
import {
  BrowserRouter as Router,
  HashRouter,
  Route,
  Routes,
} from "react-router-dom";
import Home from "./views/Home";
import Login from "./views/Login";
import Dashboard from "./views/Dashboard/Dashboard";
import { AuthContext } from "./utils/AuthContext";
import Authorization from "./components/Authorization";
import { Box, ThemeProvider, Typography } from "@mui/material";
import { ThemeContext } from "./utils/ThemeContext";
import Notes from "./views/Dashboard/Notes";
import EditNote from "./views/Dashboard/EditNote";
import PublicNotes from "./views/PublicNotes";
import About from "./views/About";
import Project from "./views/Project";
import PublicNote from "./views/PublicNote";

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
        <Route path="notes" element={<PublicNotes />} />
        <Route path="notes/note" element={<PublicNote />} />
        <Route path="about" element={<About />} />
        <Route path="project" element={<Project />} />
        <Route path="login" element={<Login setLoginToken={setJwt} />} />
        <Route path="dashboard" element={
          <Authorization>
            <Dashboard>
              <Typography variant="h4" color="white">notes</Typography>
              <Notes />
            </Dashboard>
          </Authorization>
        } />
        <Route path="dashboard/edit-note" element={
          <Authorization>
            <Dashboard>
              <EditNote />
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
          width: "calc(100% - 10px)",
          minHeight: "calc(100vh - 10px)",
          display: "flex",
          flexDirection: "column",
          bgcolor: "secondary.main",
          border: "5px solid #42b883"
        }}
      >
        <HashRouter>
          <AppRoutes />
        </HashRouter>
      </Box>
    </ThemeProvider>
  );
};

export default App;
