import streamlit as st
import streamlit.components.v1 as components


components.html(
    """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                
            </style>
        </head>
        <body>
            <!-- Navbar HTML -->
            <div class="navbar">
                <a href="#" class="logo">My Website</a>
                <a href="#">Home</a>
                <a href="#">About</a>
                <a href="#">Services</a>
                <a href="#">Portfolio</a>
                <a href="#">Contact</a>
            </div>

            <!-- Content goes here -->

        </body>
        </html>

    """,
    
)