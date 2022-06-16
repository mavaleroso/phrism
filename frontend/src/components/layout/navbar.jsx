import * as React from "react";
import Head from "next/head";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Avatar from "@mui/material/Avatar";
import IconButton from "@mui/material/IconButton";
import GlobalStyles from "@mui/material/GlobalStyles";
import Container from "@mui/material/Container";
import Menu from "@mui/material/Menu";
import MenuItem from "@mui/material/MenuItem";
import ArrowDown from "@mui/icons-material/ArrowDropDown";

function Navbar() {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };
  return (
    <React.Fragment>
      <Head>
        <title>City Government of Pilar</title>
      </Head>
      <GlobalStyles styles={{ ul: { margin: 0, padding: 0, listStyle: "none" } }} />
      <CssBaseline />
      <AppBar
        position="fixed"
        elevation={0}
        className="landing-page"
        sx={{
          color: `white`,
          backgroundColor: `#222328`,
          borderBottom: (theme) => `1px solid ${theme.palette.divider}`,
        }}
      >
        <Container maxWidth="lg">
          <Toolbar variant="dense" sx={{ flexWrap: "wrap" }}>
            {/* <Typography variant="h6">Marwen name</Typography> */}
            <Box sx={{ flexGrow: 1 }}>
              <IconButton sx={{ p: 0 }}>
                <Avatar alt="Remy Sharp" src="/static/images/logo.png" />
              </IconButton>
            </Box>
            <Typography component="div" sx={{ alignSelf: "flex-end" }}>
              <Box sx={{ flexGrow: 1, display: { xs: "none", md: "flex" } }}>
                <Button key="Home" sx={{ my: 1, color: "white", display: "block" }} size="small">
                  Home
                </Button>
                <div>
                  <Button
                    key="City Info"
                    sx={{ my: 1, color: "white" }}
                    aria-controls={open ? "basic-menu" : undefined}
                    // aria-haspopup="true"
                    // aria-expanded={open ? "true" : undefined}
                    onClick={handleClick}
                    endIcon={<ArrowDown />}
                    size="small"
                  >
                    City Info
                  </Button>
                  <Menu
                    anchorEl={anchorEl}
                    open={open}
                    onClose={handleClose}
                    MenuListProps={{
                      "aria-labelledby": "basic-button",
                    }}
                  >
                    <MenuItem onClick={handleClose}>Profile</MenuItem>
                    <MenuItem onClick={handleClose}>My account</MenuItem>
                    <MenuItem onClick={handleClose}>Logout</MenuItem>
                  </Menu>
                </div>
                <Button
                  key="Services"
                  sx={{ my: 1, color: "white" }}
                  endIcon={<ArrowDown />}
                  size="small"
                >
                  Services
                </Button>
                <Button
                  key="Business"
                  sx={{ my: 1, color: "white" }}
                  endIcon={<ArrowDown />}
                  size="small"
                >
                  Business
                </Button>
                <Button
                  key="Publications"
                  sx={{ my: 1, color: "white", display: "block" }}
                  size="small"
                >
                  Publications
                </Button>
                <Button key="GAD" sx={{ my: 1, color: "white", display: "block" }} size="small">
                  GAD
                </Button>
                <Button key="full_disclosure" sx={{ my: 1, color: "white", display: "block" }} size="small">
                  Full Disclosure
                </Button>
              </Box>
            </Typography>
            <Button sx={{ my: 1 }} variant="contained" size="small">
              Login
            </Button>
          </Toolbar>
        </Container>
      </AppBar>
      {/* Hero unit */}
      {/* <Container disableGutters maxWidth="sm" component="main" sx={{ pt: 8, pb: 6 }}></Container> */}
      {/* End hero unit */}
      <Container maxWidth="md" component="main"></Container>
      {/* Footer */}

      {/* End footer */}
    </React.Fragment>
  );
}

export default function landing() {
  return <Navbar />;
}
