import { ReactElement, ReactNode, useContext, useEffect } from "react";
import { AuthContext } from "../utils/AuthContext";
import { useNavigate } from "react-router-dom";

type Props = {
  children: ReactNode;
}

const Authorization = ({ children }: Props): ReactElement => {
  const history = useNavigate();
  const jwtContext: string = useContext(AuthContext);

  useEffect(() => {
    if (!jwtContext) {
      history("/login");
    }
  }, [jwtContext, history]);
  return (
    <>
      {children}
    </>
  );
};

export default Authorization;
