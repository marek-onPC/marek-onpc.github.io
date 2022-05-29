import { LoadingButton } from "@mui/lab";
import { Box, TextField } from "@mui/material";
import { ChangeEvent, ReactElement, SetStateAction, useState } from "react";
import { useNavigate } from "react-router-dom";
import { AuthCredentials } from "../types";
import { fetchClientPostWithoutToken } from "../utils/fetchClient";

type Props = {
  setLoginToken: SetStateAction<any>;
}

const Login = ({ setLoginToken }: Props): ReactElement => {
  const [user, setUser] = useState<AuthCredentials>(
    {
      username: "",
      password: ""
    }
  );
  const [isLoginInProgress, setIsLoginInProgress] = useState<boolean>(false);
  const history = useNavigate();

  const updateUsername = (event: ChangeEvent<HTMLInputElement>): void => {
    setUser(prevState => ({
      ...prevState,
      username: event.target.value
    }));
  };

  const updatePassword = (event: ChangeEvent<HTMLInputElement>): void => {
    setUser(prevState => ({
      ...prevState,
      password: event.target.value
    }));
  };

  const login = async (): Promise<void> => {
    setIsLoginInProgress(true);

    try {
      const request = await fetchClientPostWithoutToken(
        "/login",
        user
      );
      setIsLoginInProgress(false);

      if (request.status === 200) {
        setLoginToken(request.data.token);

        history("/dashboard");
      }
    }
    catch (error) {
      console.log(error)
      setIsLoginInProgress(false);
    }
  };

  return (
    <div>
      <Box
        sx={{
          width: "100%",
          height: "100vh",
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
            justifyContent: "center",
            '& > div': { width: "100%", maxWidth: 250, margin: 1 },
          }}
        >
          <TextField
            helperText="Enter you username and password"
            label="Username"
            onChange={updateUsername}
          />
          <TextField
            label="Password"
            type="password"
            onChange={updatePassword}
          />
        </Box>
        <LoadingButton sx={{
          width: 150,
          margin: "50px auto 0"
        }}
          onClick={login}
          variant="contained"
          loading={isLoginInProgress}>
          Loading
        </LoadingButton>
      </Box>
    </div>
  );
};

export default Login;
