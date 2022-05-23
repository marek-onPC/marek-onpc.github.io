import { ReactElement, ReactNode, useContext, useEffect } from "react";
import { AuthContext } from "../utils/AuthContext";
import { useNavigate } from "react-router-dom";
import { DynamicContext } from "../types";

type Props = {
  children: ReactNode;
}

const Authorization = ({ children }: Props): ReactElement => {
  const history = useNavigate();
  const jwtContext: DynamicContext = useContext(AuthContext);

  useEffect(() => {
    if (!jwtContext.jwt) {
      history("/login");
    }
  }, [jwtContext.jwt, history]);
  return (
    <>
      {children}
    </>
  );
};

export default Authorization;