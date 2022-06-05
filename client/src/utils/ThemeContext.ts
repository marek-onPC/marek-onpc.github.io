import { createTheme, responsiveFontSizes } from "@mui/material/styles";

let ThemeContext = createTheme({
  palette: {
    primary: {
      main: "#42b883",
    },
    secondary: {
      main: "#35495e",
    },
    action: {
      disabledBackground: "#42b883",
    },
  },
  typography: {
    fontFamily: `-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans- serif`,
  },
  components: {
  MuiButton: {
    styleOverrides: {
      root: {
        color: "#fff",
        fontWeight: 600,
      },
    },
  },
},
});

ThemeContext = responsiveFontSizes(ThemeContext);

export { ThemeContext };