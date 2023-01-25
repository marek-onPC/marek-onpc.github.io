import { ReactElement } from "react";
import { Card, CardContent, Typography, useTheme } from "@mui/material";
import { NoteCardType } from "../types";
import { Link } from "react-router-dom";

interface Props extends NoteCardType { isDashboard?: boolean, isGreen?: boolean }

const NoteCard = ({ id, title, categories, isDashboard = false, isGreen = false }: Props): ReactElement => {
  const URL = isDashboard ? `edit-note?id=${id}` : `note?id=${id}`;
  const theme = useTheme();

  return (
    <Link to={URL} style={{ textDecoration: "none", margin: "10px", width: isDashboard ? "auto" : "31%" }}>
      <Card sx={{ height: "100%", minWidth: 275, background: isGreen ? theme.palette.primary.main : null }}>
        <CardContent>
          <Typography variant="h5" component="div" sx={{ color: isGreen ? "#fff" : null, fontWeight: 600 }}>
            {title}
          </Typography>
          <Typography sx={{ mb: 1.5, color: isGreen ? "#fff" : null, fontSize: "14px" }}>
            {categories ? categories.map(category => {
              return (
                <span key={category}>{category} </span>
              )
            }) : null}
          </Typography>
        </CardContent>
      </Card>
    </Link>
  )
}

export default NoteCard;