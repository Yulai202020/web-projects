import { Button, Grid, styled } from '@mui/material';

interface GridOperationButtonProps {
    opearion: string;
    selectOpetion: ( operation: string ) => void;
    selectedOperation: string;
}

const StyledButton = styled(Button)<{selected: boolean}>((props) => ({
    backgroundColor: 'rgb(254,241,73,.1)',
    borderColor:props.selected ? '#fff' : 'rgba(254,241,73,0.5)'

}));


export const GridOperationButton:React.FC<GridOperationButtonProps> = ({
    opearion,
    selectOpetion,
    selectedOperation
}) => {
    return (
        <Grid item>
            <StyledButton fullWidth variant="outlined" onClick={()=>selectOpetion(opearion)} selected={selectedOperation == opearion}>
                {opearion}
            </StyledButton>
        </Grid>
    )
};