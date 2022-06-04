import { createTheme } from "@mui/material/styles";

export const ThemeContext = createTheme({
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