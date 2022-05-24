import { ReactElement, useEffect, useContext } from "react";
import { fetchClientGet } from "../utils/fetchClient";
import { AuthContext } from "../utils/AuthContext";
import { DynamicContext } from "../types";

const Dashboard = (): ReactElement => {
  const token: DynamicContext = useContext(AuthContext);

  const getUserName = async () => {
    try {
      const response = await fetchClientGet(
        "/authpath",
        token.jwt.token
      );

      console.log(response)
    }
    catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    getUserName()
  });

  return (
    <div>
      Dashboard
    </div>
  );
};

export default Dashboard;