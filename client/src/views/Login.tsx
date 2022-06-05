import { LoadingButton } from "@mui/lab";
import { Alert, Box, TextField } from "@mui/material";
import { ChangeEvent, ReactElement, SetStateAction, useState } from "react";
import { useNavigate } from "react-router-dom";
import { AuthCredentials } from "../types";
import { fetchClientPostWithoutToken } from "../helpers/fetchClient";

type Props = {
  setLoginToken: SetStateAction<any>;
}

const Login = ({ setLoginToken }: Props): ReactElement => {
  const [user, setUser] = useState<AuthCredentials>(
    {
      username: "",
      password: "",
    }
  );
  const [isLoginError, setIsLoginError] = useState<boolean>(false);
  const [isLoginInProgress, setIsLoginInProgress] = useState<boolean>(false);
  const history = useNavigate();

  const updateUsername = (event: ChangeEvent<HTMLInputElement>): void => {
    setUser(prevState => ({
      ...prevState,
      username: event.target.value,
    }));
  };

  const updatePassword = (event: ChangeEvent<HTMLInputElement>): void => {
    setUser(prevState => ({
      ...prevState,
      password: event.target.value,
    }));
  };

  const login = async (): Promise<void> => {
    setIsLoginInProgress(true);
    setIsLoginError(false);

    try {
      const response = await fetchClientPostWithoutToken(
        "/login",
        user
      );

      setIsLoginInProgress(false);
      setLoginToken(response.data.token);
      history("/dashboard");

    } catch (error) {
      console.error(error);
      setIsLoginInProgress(false);
      setIsLoginError(true);
    }
  };

  return (
    <Box
      sx={{
        width: "100%",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
      }}
    >
      <Box
        component="form"
        sx={{
          width: "100%",
          display: "flex",
          flexWrap: "wrap",
          justifyContent: "center",
          paddingTop: "200px",
          '& > div': { width: "100%", maxWidth: 250, margin: 1 },
        }}
      >
        <TextField
          sx={{
            backgroundColor: "#fff",
            borderRadius: 1
          }}
          variant="filled"
          label="Username"
          onChange={updateUsername}
        />
        <TextField
          sx={{
            backgroundColor: "#fff",
            borderRadius: 1
          }}
          variant="filled"
          label="Password"
          type="password"
          onChange={updatePassword}
        />
      </Box>
      <LoadingButton
        sx={{
          width: 150,
          margin: "50px auto 0"
        }}
        onClick={login}
        variant="contained"
        loading={isLoginInProgress}
      >
        Login
      </LoadingButton>
      {isLoginError
        ? <Alert
          sx={{
            width: "100%",
            maxWidth: 250,
            margin: "50px auto 0"
          }}
          severity="error"
        >
          Error occurred on login, try again.
        </Alert>
        : null}
    </Box>
  );
};

export default Login;
