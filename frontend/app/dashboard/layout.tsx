'use client'

import SideNav from '../component/sidebar'
import { Box, Flex } from "@chakra-ui/react";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
    return (
        <html lang="en">
          <body>
          <Flex>
          <SideNav />
          <Box flex="5" pl="10">
            {children}
          </Box>
        </Flex>
          </body>
        </html>
      )
}
