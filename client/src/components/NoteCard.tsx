import { ReactElement } from "react";
import { Card, CardContent, Typography } from "@mui/material";
import { NoteCardType } from "../types";
import { Link } from "react-router-dom";

interface Props extends NoteCardType { isDashboard?: false }

const NoteCard = ({ _id, title, categories, isDashboard = false }: Props): ReactElement => {
  const URL = `note?id=${_id}`;

  return (
    <Link to={URL} style={{ textDecoration: "none", margin: "10px" }}>
      <Card sx={{ minWidth: 275 }}>
        <CardContent>
          <Typography variant="h5" component="div">
            {title}
          </Typography>
          <Typography sx={{ mb: 1.5 }} color="text.secondary">
            {categories.map(category => {
              return (
                <span key={category}>{category} </span>
              )
            })}
          </Typography>
        </CardContent>
      </Card>
    </Link>

  )
}

export default NoteCard;