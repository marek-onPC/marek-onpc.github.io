import { ReactElement, SetStateAction } from "react";
import { useNavigate } from "react-router-dom";
import { HTTPMethods } from "../types";
import { fetchClientWithoutToken } from "../utils/fetchClient";

type Props = {
  setLoginToken: SetStateAction<any>;
}

const Login = ({ setLoginToken }: Props): ReactElement => {
  const history = useNavigate();


  const login = async (): Promise<any> => {
    try {
      const jwt = await fetchClientWithoutToken(
        "/login",
        HTTPMethods.POST,
        { credentials }
      );

      setLoginToken(jwt);
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