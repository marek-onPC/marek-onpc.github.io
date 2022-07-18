import { ButtonGroup, Container, Button, Box } from "@mui/material";
import { ReactElement, ReactNode } from "react";
import { Link } from "react-router-dom";

type Props = {
  children: ReactNode;
}

const Dashboard = ({ children }: Props): ReactElement => {
  return (
    <Container
      sx={{
        width: "100%",
        display: "flex",
        flexWrap: "wrap",
        justifyContent: "center",
        paddingTop: "50px",
      }}
      maxWidth="xl"
    >
      <ButtonGroup variant="contained">
        <Button>
          <Link
            style={{
              color: "inherit",
              textDecoration: "none",
            }}
            to="/dashboard"
          >
            Notes
          </Link>
        </Button>
        <Button
          onClick={() => {
            window.localStorage.removeItem(
              process.env.REACT_APP_LOCAL_STORAGE_TOKEN as string
            );
            window.location.replace("/dashboard");
          }}
        >
          Logout
        </Button>
      </ButtonGroup>
      <Box
        sx={{
          width: "100%",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          paddingTop: "50px",
        }}
      >
        {children}
      </Box>
    </Container>
  );
};

export default Dashboard;
