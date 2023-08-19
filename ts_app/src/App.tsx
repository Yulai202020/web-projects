import React, { useState } from "react";
import { Container,Grid,Paper,styled } from '@mui/material';
import GirdOperationButton from './GridOperationButton'
const OutputContainer = styled('div') (({ theme })=>({
  width: "100%",
  textAlign: "right",
  height: "2em",
  padding: theme.spacing(3),
  fontSize: "3em",
  owerflow: "hidden"
}));

const CalculatorBase = styled(Paper)(({ theme })=>({
  padding: theme.spacing(2),
  marginTop: theme.spacing(4),
  borderRadius: 15
}));  

const app = () => {
  const [currentValue,setCurrentValue ] = useState("0");
  const [opearion,setOpearion ] = useState("");
  const selectOperation = (opearion:string) => {
    setOpearion(opearion);
  }
  const setDigit = (digit:string) => {
    setCurrentValue(digit)  
  }
  return (
    <Container maxWidth="sm">
      <CalculatorBase elevation={3}>
        <Grid container spacing={3}>
           <Grid item xs={12}>
            <OutputContainer>
              {currentValue}
            </OutputContainer>
           </Grid>
           <Grid item container columnSpacing={1}>
            <GirdOperationButton operation={'AC'} selectOperation>

            </GirdOperationButton>
           </Grid>
        </Grid>
      </CalculatorBase>
    </Container>
  );
}
export default app;