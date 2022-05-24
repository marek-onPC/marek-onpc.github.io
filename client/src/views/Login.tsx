import { ReactElement, SetStateAction } from "react";
import { useNavigate } from "react-router-dom";
import { fetchClientPostWithoutToken } from "../utils/fetchClient";

type Props = {
  setLoginToken: SetStateAction<any>;
}

const Login = ({ setLoginToken }: Props): ReactElement => {
  const history = useNavigate();

  const login = async (): Promise<void> => {
    try {
      const jwt = await fetchClientPostWithoutToken(
        "/login",
        { credentials }
      );

      setLoginToken(jwt.token);
      history("/dashboard");
    }
    catch (error) {
      console.log(error)
    }
  }

  return (
    <div>
      Login
      <p onClick={login}>Click to login</p>
    </div>
  );
};

export default Login;
