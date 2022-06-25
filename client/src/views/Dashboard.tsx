import { ButtonGroup, Container, Button, Box } from "@mui/material";
import { ReactElement, useEffect, useContext, ReactNode } from "react";
import { Link } from "react-router-dom";
import { fetchClientGet } from "../helpers/fetchClient";
import { AuthContext } from "../utils/AuthContext";

type Props = {
  children: ReactNode;
}

const Dashboard = ({ children }: Props): ReactElement => {
  const token: string = useContext(AuthContext);

  const getUserName = async (): Promise<void> => {
    try {
      const response = await fetchClientGet(
        "/authpath",
        token
      );

      console.log(response);
    }
    catch (error) {
      console.log(error);
    }
  }

  useEffect(() => {
    getUserName();
  });

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
            to="/dashboard/notes"
          >
            Notes
          </Link>
        </Button>
        <Button>
          <Link
            style={{
              color: "inherit",
              textDecoration: "none",
            }}
            to="/dashboard/categories"
          >
            Categories
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
